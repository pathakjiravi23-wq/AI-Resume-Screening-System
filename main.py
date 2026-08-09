from pathlib import Path
from reader import text_file, pdf_file, docx_file
from preprocessor import clean_text

READER = {".txt": text_file, ".pdf": pdf_file, ".docx": docx_file}


def document(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError("file not found")
    reader = READER.get(path.suffix)
    if reader is None:
        raise ValueError("Unsupported file")
    return reader(file_path)  # suppose reader=pdf_file so it call pdf_file(file_path)


def main():
    path = input("Enter file adderess : ")
    try:
        doc_data = document(path)
        clean_data = clean_text(doc_data)
        print(clean_data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
