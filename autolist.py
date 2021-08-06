import csv
remark0 = ''
inum = 1
iname = 2
iremark = 5
imail = 7
snum = 1
sname = 2
smail = 3
googlecontacts = ['Name', 'E-mail 1 - Value', 'Group Membership', 'Notes']
namelist = []
print('Welcome! v1.A46')

def setheader(filename):
    with open(filename + '.csv', 'r', encoding='utf-8-sig') as f:
        header = next(csv.reader(f))
        del header[0]
    return header


def readf(filename):
    data = []
    with open(filename + '.csv', 'r', encoding='utf-8-sig') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            data.append(line)
    return data


def chkinum(lines):
    for line in lines:
        line[inum] = line[inum].upper()
        line[inum] = line[inum].replace('O', '0')
    return lines

def sortab(lines):
    dataa = []
    datab = []
    for line in lines:
        if line[iremark]== remark0:
            dataa.append(line)
        else:
            datab.append(line)
    return [dataa, datab]


def addmail(solines, inlines):
    for i in inlines:
        for s in solines:
            if i[iname]==s[sname]:
                if i[inum]==s[snum]:
                    if s[smail] != '':
                        i.append(True)
                        i.append(s[smail])
                        i.append('')
                        break
                    else:
                        i.append(None)
                        i.append(s[smail])
                        i.append('此人無mail')
                        break
                else:
                    if s[smail] != '':
                        i.append(True)
                        i.append(s[smail])
                        i.append('是否為' + s[snum] + s[sname])
                    else:
                        i.append(None)
                        i.append(s[smail])
                        i.append('是否為' + s[snum] + s[sname] + '此人無mail')
            elif i[iname][:3] == s[sname]:
                i.append(True)
                i.append(s[smail])
                i.append('是否為' + s[snum] + s[sname])
            elif i[iname][:4] == s[sname]:
                i.append(True)
                i.append(s[smail])
                i.append('是否為' + s[snum] + s[sname])
        if len(i) < imail:
            i.append(False)
            i.append('')
            i.append('查無此人')
    return inlines


def makedata(lines, group):
    datag = []
    for line in lines:
        d = []
        if line[imail-1]:
            d.append(line[iname])
            d.append(line[imail])
            d.append(group)
            d.append(line[imail+1])
            datag.append(d)
    datae = []
    for line in lines:
        d = []
        for i in range(1, 5):
            d.append(line[i])
        if line[imail-1]:
            d.append('')
        elif line[imail-1]==None:
            d.append('此人無mail')
        else:
            d.append('查無mail')
        datae.append(d)
    return [datag, datae]


def writef(lines, filename, header):
    with open(filename + '.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(lines)
    return True


def printls(lines):
    for line in lines:
        print(line)


def main():
    namelist=setheader('input')
    d = sortab(chkinum(readf('input')))
    da = makedata(addmail(readf('Source'),d[0]), 'A')
    db = makedata(addmail(readf('Source'),d[1]), 'B')
    #printls(da[1])
    if writef(da[1],'A會議室名單', namelist):
        print('A會議室名單,檔案成功產出')
    if writef(da[0] + db[0],'google通訊錄', googlecontacts):
        print('google通訊錄,檔案成功產出')

main()
