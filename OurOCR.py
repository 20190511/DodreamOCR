import os
import dotenv
import BetterOCR.betterocr.__init__

OPENAPI_KEY = ""


def getImg(path="Img"):
    ret_flist = []
    for a, b, c in os.walk(path):
        for item in c:
            ret_flist.append(os.path.join(a, item))
    return ret_flist

def api(idx):
    global OPENAPI_KEY
    print(f"Hello, your key : {dotenv.load_dotenv('OPENAI_API_KEY')}")
    fList = getImg()

    image_path = fList[idx]

    text = BetterOCR.betterocr.detect_text(
        image_path,
        ["ko", "en"],  # language codes (from EasyOCR)
        context="",  # (optional) context
        tesseract={
            # Tesseract options here
            "config": "--tessdata-dir ./tessdata"
        },
        openai={
            # OpenAI options here

            # `os.environ["OPENAI_API_KEY"]` is used by default
            "API_KEY": OPENAPI_KEY,
            # rest are used to pass params to `client.chat.completions.create`
            # `{"model": "gpt-4"}` by default
            "model": "gpt-4o-mini",
        },
    )

    print("return --- > ")
    return text


if __name__ == "__main__":
    dotenv.load_dotenv()
    OPENAPI_KEY = os.environ.get("OPENAI_API_KEY")
    print(api(4))