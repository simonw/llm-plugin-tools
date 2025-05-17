import llm
import json
from {{ cookiecutter.underscored }} import {{ cookiecutter.function_name }}


def test_tool():
    model = llm.get_model("echo")
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {"name": "{{ cookiecutter.function_name }}", "arguments": {"input": "pelican"}}
                ]
            }
        ),
        tools=[{{ cookiecutter.function_name }}],
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {"name": "{{ cookiecutter.function_name }}", "output": "hello pelican", "tool_call_id": None}
    ]
