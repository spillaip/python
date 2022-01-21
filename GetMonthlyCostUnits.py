#
#
# Get Unique schemes
# For each scheme get cost, units
# Get Unique Periods Months and Years
# print unique scheme, cost, and units
#
import csv

units = 0.00
t_cost = 0.00
t_units = 0.00
r_result = []
periods = []
_file = 'suresh-trx.csv'
_outfile = 'suresh-trx-out.csv'
_data = []


def getData():
    tmpdata = []
    # print('Reading file and loading')
    with open(_file, 'r') as csv_sud_trx:
        csv_reader = csv.reader(csv_sud_trx)
        tmpdata = list(csv_reader)
    csv_sud_trx.close()
    tmpdata.pop(0)
    return tmpdata


def getSchemes(_idata):
    schemes = list()
    #print('Length of list is', _idata.__len__(), 'Type is ', type(_idata))
    # changed from processing file to a list
    for _lines in _idata:
        # print('printing _lines:',_lines)
        schemes.append(_lines[5])
        set_schemes = set(schemes)
        unique_schemes = list(set_schemes)
        unique_schemes.sort()

    # csv_sud_trx.close()
    return unique_schemes


def getCost(_ischeme, _period, _idata):
    _cost = 0.00
    _units = 0.00
    _price = 1
    _retval = []
    #use comprehension to reduce
    #the number of transactions
    #for more efficient processing
    #_reducedTrx = [_trx for _trx in _idata if _idata[5][5]==_ischeme and _idata[6][3:]==_period]

    #loop the reduced transaction set
    #obtain cost
    # units
    # average price
    # store them in a list and return
    # 4 scheme_code
    # 5 scheme_name
    # 6 trx_date
    # 7 trx_type
    # 8 div_amt
    # 9 trx_amount
    # 10 trx_unit
    # 11 trx_price
    #print('scheme got is:', _ischeme, 'period', _period)
    #filtered_list = [fl for fl in _idata if _idata[5]==_ischeme and _idata[6][3:]==_period]
    #print('filetered list size is ',(filtered_list).__sizeof__())
    #for i in filtered_list:
    #    print('filtered list content is',i)
    _idata.pop()
    for trx in _idata :
        #print('data for is scheme:', trx[5], 'period', trx[6], 'amount:', trx[9], 'units:', trx[10])
        if (trx[5]==_ischeme and trx[6][3:]== _period):
            #print('inside scheme got is:', trx[5], 'period got is', trx[6], 'amount is',trx[9], 'units are',trx[10])
            if trx[9] != "" and trx[10] != "":
                _tcost = trx[9].replace(" ","").strip()
                _tunits = trx[10].replace(" ","").strip()
                #print(trx[4], trx[5], trx[6], trx[7], trx[8], trx[9], trx[10], trx[11], trx[12])
                #print('-',_tcost,'-', _tunits)
                #print('inside -', trx[9], '-', trx[10])
                if trx[9] != "" and trx[10] != "" and trx[9] != 'AMOUNT':
                    #print('before adding to _cost')
                    _cost = _cost + float(_tcost)
                    _units = _units + float(_tunits)
                    #print('_cost=',_cost, '_units', _units)

        #print(_ischeme,_cost,_units)
        _price = 1 #(1+(float(_units)/float(_cost)))
    _retval.append(_ischeme)
    _retval.append(_period)
    _retval.append(_cost)
    _retval.append(_units)
    _retval.append(_price)
    return _retval




#
# Get periods for a given scheme
# Use the data array instead
def getPeriods(i, _data):
    _period=[]
    _uniquePeriods=[]

    for j in _data:
        if (i.strip()==j[5]):
            #print(j[5], j[6])
            _period.append(j[6][3:])

    _uniquePeriods = list(set(_period))
    _uniquePeriods.sort()
    #print(_uniquePeriods)
    return _uniquePeriods

#Main logic is here

# writing to csv file
with open(_outfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    _data = getData()
    #print(_data[5])
    schemes = getSchemes(_data)

    for i in schemes:
        print(i)
        periods = getPeriods(i, _data)
        for _period in periods:
            r_result = getCost(i,_period,_data)
            #print(r_result)
            # writing the data rows
            csvwriter.writerow(r_result)
#csvfile.close()
