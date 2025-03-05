from openai import OpenAI
from fastapi import UploadFile,File,HTTPException
from pypdf import PdfReader 
from helper.chunk import get_chunk
import io
from ..helper.db import get_db
from dotenv import load_dotenv
from ..model import Question
load_dotenv()

client = OpenAI()

async def question(item:Question):
    db=get_db()
    inp=item.q
    ans = db.similarity_search(inp)
    new_text=ans[0].page_content
    sys="You will be provided with a question , and your task is to answer the question using only the text: \n'"+new_text+".'\n if answer is not found in the data,answer 'I dont know'."
    print(sys)
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": sys
        },
        {
          "role": "user",
          "content": inp
        }
      ],
      temperature=0.3,
      max_tokens=200,
      top_p=1
    )
    return {"response":response.choices[0].message.content}
        

async def upload( file:UploadFile=File(...)):
     db=None
     name=str(file.filename)
     if(name.endswith(".pdf")):
        file_content = await file.read()
        read = PdfReader(io.BytesIO(file_content))
        text=""
        for page in read.pages:
            text+=page.extract_text() 
        print(len(text))
        db=get_chunk(text)
        return {"message":"uploaded successfully"}
        
     else:
         raise HTTPException(status_code=422,detail="invalid file")


     


   