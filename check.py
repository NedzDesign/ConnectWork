import g4f

response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Hello"}],
    proxy="http://BQ6K7x:BsEUjy@138.99.37.42:9526"

)  # alternative model setting

print(response)