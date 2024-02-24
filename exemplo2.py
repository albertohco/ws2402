from pydantic import BaseModel


class calc(BaseModel):
    x: int
    y: int


external_data = {'x': '10', 'y': '2'}
numeros = calc(**external_data)
resultado = numeros.x + numeros.y
print(resultado)
