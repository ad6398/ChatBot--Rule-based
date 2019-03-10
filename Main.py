import json
from pprint import pprint
import inquirer
print("input filepath")
filepath= input()
with open(filepath) as dtf:    
    data = json.load(dtf)
# pprint(data)
global rows, matrix
que= data["questions"]
globals().update(locals())
for ins in que:
    # print(type(ins))
    inst= ins.get("instruction", False)  # text only
    option= ins.get("options", False)  #list
    txt= ins.get("text", False)        # text string
    var= ins.get("var", False)         # single var
    cond= ins.get("conditions", False)     # list of list of condition
    frm= ins.get("formula", False)        # needed to excute single line
    cal_var= ins.get("calculated_variable", False) # bool if cal in variable is envolved
    ins_var= ins.get("instruction_var", False)  #list of variable involve in printing instruction
    ls_var= ins.get("list_var", False)
    ls_len= ins.get("lis_length", False)


    

    if(inst):
        # print(inst, "yha")
        if(ins_var):
            itr=1
            if(ls_var):
                if(eval(ls_var)):
                    itr= int(ls_len)
            for i in range(itr):
                    pr= inst
                    for x in ins_var:
                        y=globals()[x]
                        pr=pr % (y)
                    print(pr)
                
        else:
            print(inst)
    
    if(cond):
        tr= False
        for condition in cond:
            tem= True
            for x in condition:
                # print(x)
                # print(eval(x))
                if(eval(x)):
                    tem=False
                # print(vl, "excu val")
                # tem= (tem and vl)
            tr= tr or tem
        if(tr==False):
            if(txt):
                print(txt)
                if(option):
                    qs= [ inquirer.List("gender", message="give ",choices=option),]
                    ans= inquirer.prompt(qs)
                    globals()[var]= ans["gender"]
                else:
                    globals()[var]= input()
    
    if(txt and cond==False):
         print(txt)
        #  print(var)
         
         if(option):
            qs= [ inquirer.List("gender", message="",choices=option),]
            ans= inquirer.prompt(qs)
            globals()[var]= ans["gender"]
         else:
             globals()[var]= input()
            


    if(cal_var):
        if(eval(cal_var)):
            globals()[var]= eval(frm)

    







