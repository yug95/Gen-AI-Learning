import Groq from "groq-sdk";

import readline from "readline";

const groq = new Groq({ apiKey: process.env.groq_api_key });

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const IncomeDB = [];
const ExpenseDB = [];
async function callAgent() {
  const messageList = [
    {
      role: "system",
      content: `You are Player-456, a personal finance assistant and help with my finances.
                You have access to these tools nad call only when needed :
                1.addIncome({name, amount})  to add income to the database
                2.getExpense({fromdate, toDate})  to get the expenses from the database
                3.addExpense({name, amount }) to add expense to the database 
       `,
    },
  ];

  //  loop for user follow up question
  while (true) {
    const userQuestion = await userInput("user: ");
    if (userQuestion == "bye") {
      rl.close();
      break;
    }

    messageList.push({
      role: "user",
      content: userQuestion,
    });

    // loop for tools
    while (true) {
      const response = await groq.chat.completions.create({
        messages: messageList,
        model: "llama-3.1-8b-instant",
        tools: [
          {
            type: "function",
            function: {
              name: "getExpense",
              description:
                "function to get the total expense from todate to fromdate",
              parameters: {
                type: "object",
                properties: {
                  fromdate: {
                    type: "string",
                    description: "The start date for the expense calculation",
                  },
                  todate: {
                    type: "string",
                    description: "The end date for the expense calculation",
                  },
                },
              },
            },
          },

          {
            type: "function",
            function: {
              name: "addIncome",
              description: "tool to add the income to the database",
              parameters: {
                type: "object",
                properties: {
                  name: {
                    type: "string",
                    description: "name of the income. e.g got salary",
                  },
                  amount: {
                    type: "string",
                    description: "amount received e.g 20000 INR",
                  },
                },
              },
            },
          },

          {
            type: "function",
            function: {
              name: "addExpense",
              description: "tool to add the income to the database",
              parameters: {
                type: "object",
                properties: {
                  name: {
                    type: "string",
                    description: "name of the expense. e.g bought a car",
                  },
                  amount: {
                    type: "string",
                    description: "amount spent e.g 20000 INR",
                  },
                },
              },
            },
          },
        ],
      });
      messageList.push(response.choices[0].message);

      const toolcall = response.choices[0].message.tool_calls;
      if (!toolcall) {
        console.log(
          `${response.choices[0].message.role}: ${response.choices[0].message.content}: `
        );
        break;
      }

      for (const tool of toolcall) {
        const functionName = tool.function.name;
        const functionArgument = tool.function.arguments;
        let result = "";
        if (functionName == "getExpense") {
          result = getExpense(JSON.parse(functionArgument));
          messageList.push({
            role: "tool",
            tool_call_id: tool.id,
            content: result.toString(),
          });
        }
        if (functionName == "addExpense") {
          result = addExpense(JSON.parse(functionArgument));
          messageList.push({
            role: "tool",
            tool_call_id: tool.id,
            content: result.toString(),
          });
        }

        if (functionName == "addIncome") {
          result = addIncome(JSON.parse(functionArgument));
          messageList.push({
            role: "tool",
            tool_call_id: tool.id,
            content: result,
          });
        }
      }
    }
  }
}

function getExpense({ toDate, fromDate }) {
  console.log("getting the expance......");

  return 10;
}

function addExpense({ name, amount }) {
  ExpenseDB.push(`${name} ${amount}`);
  console.log(ExpenseDB);
  return `Expense add of ${name} of ${amount}`;
}

function addIncome({ name, amount }) {
  console.log("adding income to the database");
  IncomeDB.push(`${name}  ${amount}`);
  console.log(IncomeDB);
  return `${amount} add to the income as ${name}`;
}

callAgent();

function userInput(query) {
  return new Promise((resolve) => rl.question(query, resolve));
}
