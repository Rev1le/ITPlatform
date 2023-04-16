import edgedb

query = """
insert TaskBlock {
  name := "Основы Python",
  difficulty := 0,
  description := "Так сказать база",
  questions := {
    (insert TaskQuestion {
      question := "Что напечатает следующий код print((1 ,2, 3)<(1, 2, 4))",
      answers := <array<str>>["None", "True", "False", "Ошибка"],
      right_answer := "True"
    }),
    (insert TaskQuestion {
      question := "Какое значение получит a? a = 2,3",
      answers := <array<str>>["2", "3", "(2, 3)"],
      right_answer := "(2, 3)"
    }),
    (insert TaskQuestion {
      question := "Где правильно создана переменная?",
      answers := <array<str>>["int num = 2", "$num = 2", "var num = 2", "num = float(2)", "Нет"],
      right_answer := "num = float(2)"
    })
  },
  codes := (
    insert TaskCode {
      question := "Напишите программу складывающую два переданных через пробел числа",
      tests := {
        (insert TaskCodeTest {
          input := "2 2",
          output := "4"
        }),
        (insert TaskCodeTest {
          input := "5 5",
          output := "10"
        })
      }
    }
  )
};
"""

answer = """
{
  "questions": [
    {
      "id": "3a420d92-dbfa-11ed-933e-63427b776b07",
      "answer": "True"
    },
    {
      "id": "3a4220ca-dbfa-11ed-933e-c3149917a563",
      "answer": "(2, 3)"
    },
    {
      "id": "3a4224b2-dbfa-11ed-933e-bb1560605df9",
      "answer": "num = float(2)"
    }
  ],
  "codes": [
    {
      "id": "3a41ee84-dbfa-11ed-933e-932746b2012e",
      "lang": "Python",
      "answer": "x, y = map(int, input().split()); print(x+y)"
    }
  ]
}
"""

client = edgedb.create_client()

for i in client.query(query):
    print(i.id)
