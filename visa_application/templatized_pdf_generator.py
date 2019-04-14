import io
import subprocess
import tempfile
from pathlib import Path


class TemplatizedPdfGenerator:
    def __init__(self, template):
        self.template = template

    def __call__(self, **kwargs):
        latex = self.template.render(**kwargs)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            latex_file = temp_dir / 'temp.tex'
            latex_file.write_text(latex)

            subprocess.run(
                [
                    'pdflatex',
                    f'-output-directory={temp_dir}',
                    str(latex_file),
                ],
                capture_output=True,
            )

            return io.BytesIO((temp_dir / 'temp.pdf').read_bytes())
