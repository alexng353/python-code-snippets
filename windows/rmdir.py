import os, shutil, errno, stat



# Remove readonly from stupid directories
def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

# actual function
def deleteFile(**kwargs):
    delete_path = kwargs['path']

    shutil.rmtree(delete_path, ignore_errors=False, onerror=handleRemoveReadonly)
    print("Removed " + delete_path + " and contents")


