import os

#script for figuring out which large files git is rejecting

def lsfilescwd(cwd):
    _mb_ = 1000000 #test value
    _5gb_ = 5000 * _mb_ #git lfs file size limit
    #print(cwd)
    pwd = ""
    for entry in os.listdir(cwd):
        if(entry):
            cfile = os.path.join(cwd, entry)
            statinfo = os.stat(cfile)
            if(os.path.isdir(cfile)):
                #print(cfile)
                pwd = cwd
                os.chdir(cfile)
                lsfilescwd(str(cfile))
            else:
                fsize = statinfo.st_size
                if(fsize > _mb_):
                    print(cfile + " " + str(statinfo.st_size / _mb_) + "MB")
            #lsfilescwd(pwd)
lsfilescwd(os.getcwd())
input()