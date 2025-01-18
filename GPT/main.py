from openai import OpenAI

def sendGPTRequest(image, address: str):
    assistant_id = "asst_gShRAai0FxG4sHmtfdlS87dx"
    client = OpenAI()

    thread = client.beta.threads.create()

    message = {

    }
