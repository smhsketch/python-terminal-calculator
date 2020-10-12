# Copyright 2020 Patrick Warren

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

print("python-calculator by smhsketch. type quit or exit to quit.")

def numSplit(word):
    return [char for char in word]

while True: 
    calculation = input("; ")
    if calculation == "exit" or calculation == "quit":
        quit()
    else:
        calcList = list(calculation)
        calcNums = [x for x in calcList if not (x.isdigit() 
                                                or x[0] == '-' and x[1:].isdigit())]
        op = calcNums[0]
        opIndex = calcList.index(op)
        calcList.pop(calcList.index(op))

        int1 = calcList[:opIndex]
        int1 = int(''.join(int1))
        int2 = calcList[opIndex:]
        int2 = int(''.join(int2))
        
        # temporary method
        if op == "*":
            ans = int1 * int2
        elif op == "/":
            ans = int1 / int2
        elif op == "+":
            ans = int1 + int2
        elif op == "-":
            ans = int1 - int2
        else:
            print("syntax error")
        
        print(ans)