from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {
        "llm-tools-foo/llm_tools_foo.py",
        "llm-tools-foo",
        "llm-tools-foo/.gitignore",
        "llm-tools-foo/tests",
        "llm-tools-foo/.github/workflows/publish.yml",
        "llm-tools-foo/README.md",
        "llm-tools-foo/.github/workflows",
        "llm-tools-foo/LICENSE",
        "llm-tools-foo/.github",
        "llm-tools-foo/pyproject.toml",
        "llm-tools-foo/tests/test_llm_tools_foo.py",
        "llm-tools-foo/.github/workflows/test.yml",
    }


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
