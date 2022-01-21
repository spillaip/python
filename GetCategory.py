import csv
import sys
from os import replace

# _inputfile = sys.argv[1]
_inputfile = 'sbi.csv'
# _outputfile = sys.argv[2]
_outputfile = 'hb_sbi.csv'
# _assigmments = sys.argv[3]
_assigmments = 'assignments.csv'
# _bank = sys.argv[4]
_bank = 'sbi'
asnmntdata = []

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print('Input File', _inputfile)
# print('Output File', _outputfile)
# print('Assignment File', _assigmments)
# print('Bank is ', _bank)


def savefinalfmt(rowdata):
    finalstr = ""
    delimiter = ","
    finallist = []
    # write finallist to csv
    # massage rowdata to homebank format


def findCategory(trx_memo):
    memostr = trx_memo
    asnmntdata = loadAssignments()
    rtndata_cat = "No Category"
    rtndata_payee = "No Payee"
    rownum=0
    flag=0

    print('Trx_memo is:', memostr, 'count of assignments are: ', len(asnmntdata))
    for _asnmntdata in asnmntdata:
        
        if(memostr.find(_asnmntdata[4])):
            print("Found",_asnmntdata[4])
            rownum=_asnmntdata
            #print("memostr is ",memostr[rownum])
            flag=1
            break
    if flag==0:
        print("not found")

    return 0


def loadTrx():
    trxData = []
    with open(_inputfile, 'r') as csv_trx:
        csv_trx_reader = csv.reader(csv_trx)
        trxData = list(csv_trx_reader)
    csv_trx.close()
    trxData.pop(0)
    return trxData


def writeTrx(trxlist):
    with open(_outputfile, 'w', newline='') as csvfile:
        csv_trx_writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_trx_writer.writerows(trxlist)
    csvfile.close()


def loadAssignments():
    asnmntdata = []
    # print('Reading file and loading')
    with open(_assigmments, 'r') as csv_assignments:
        csv_assignment_reader = csv.reader(csv_assignments)
        asnmntdata = list(csv_assignment_reader)
    csv_assignments.close()
    asnmntdata.pop(0)
    print('No of assignments are: ', len(asnmntdata))
    return asnmntdata


# asnmntdata has all the assignments
# in the form of list
asnmntdata = loadAssignments()
# for i in asnmntdata:
#    print(i)
cate = []
trxdata = loadTrx()
_fstring = []
_str = ""
_date = ""
_payment = "0"
_info = ""
_payee = ""
_memo = ""
_amount = 0.00
_category = ""
_tags = ""
for j in trxdata:
    #print("Before calling findCategory(j) ",j[2])
    cate = findCategory(j[2])
    

    # homebank format
    # date, payment(0), info, payee, memo, amount, category, tags
    # SBI
    _date = j[0]
    _payment = "0"
    _info = j[3]

    #index_pos = asnmntdata.index(j[2]) if j[2] in asnmntdata else -1
    
    print ("cate is ",cate)
    if cate > 0:
        _payee = cate[6]
        _category = cate[7]
    else:
        _payee = "No Payee"
        _category = "No Category"

    _memo = j[2]
    _dramout = j[4]
    _cramount = j[5]

    _tags = "SBI"
    _str = _date + "," + _payment + "," + _info + "," + _payee + "," + _memo + "," + _dramout + "," + _cramount + "," + _category + "," + _tags
    print("Final String is :", _str)
