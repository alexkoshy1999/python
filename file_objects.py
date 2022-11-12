    
# f = open('text.txt','r')
# print(f.name)
# print(f.mode)
# f.close()

'''another way to open file'''

# with open('text.txt','r') as f:
    # print(f.closed)
    # f_content = f.read()
    # print(f_content)
    # '''large file'''
    # f_content = f.readline()
    # print(f_content, end='')
    # f_content = f.readlines()
    # print(f_content)

    # for line in f:
    #     print(line,end='')

    # f_content = f.read(100)
    # print(f_content)

    # size_to_read = 10
    # f_content = f.read(size_to_read)
    # print(f_content,end='')

    # f.seek(0) #start from that position
    
    # f_content = f.read(size_to_read)
    # print(f_content)
    # while len(f_content) > 0:
    #     print(f_content, end='*')
    #     f_content = f.read(size_to_read)
    # print(f.tell())
# with open('text2.txt','w')as f:
#     f.write('Text')
#     f.seek(0)
#     f.write('R')
with open('text.txt','r') as rf: #rb,wb for pics
    with open('text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)
            
        
    

# print(f.name)
# print(f.closed)
# print(f.read())