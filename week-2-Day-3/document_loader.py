from pathlib import Path
from pypdf import PdfReader

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def load_document(file):

    if file is None:
        return ""

    path = Path(file.name)

    suffix = path.suffix.lower()

    if suffix == ".txt":

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    elif suffix == ".pdf":

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    return ""