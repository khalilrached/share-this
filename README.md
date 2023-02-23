### share-this

```shell
    > share-this --help
    
    Usage:
    
    share-this <command> [options]
      or
    share-this <comand> --key=value
    
    Commands:
    
    server:start                   start the server.
    server:stop                    stop the running server.
    files:add                      compress the target folder and move it to the server.
    files:list                     list all shared files.
    files:remove                   manage all files hosted on the server.
    
    Options:
    
    --version                      show version.                                                  [boolean]
    --help                         show help.                                                     [boolean]
    --silent                       run command silently.                                          [boolean]
    --verbose                      run cammand on trace level.                                    [boolean]
    -H,--hostname                  set the server hostname.                  [default: localhost] [string]
    -P,--port                      set the server port.                           [default: 6540] [number]
    -t,--target                    target file [or folder].                                       [path]
    -s,--source                    source file [or folder].                                       [path]
    
    Examples:
    
    share-this server:start # start the server on port 6540.
    share-this server:start --port=5000 # start the server on port 5000
    share-this server:start -P 5000 --silent # run server in silent mode on port 5000.
    share-this server:stop # shutdown the server.    
    
    share-this files:add # compress current directory and share it.
    share-this files:add --source=/folder/folder2 # compress folder2 and share it with the name folder2.
    share-this files:add --source=/folder/folder2 --target=download_this # compress folder2 and share it with the name 
                                                                         # download_this.
    
    share-this files:list # list all the shared files return names 
    share-this files:remove --target=folder_name
    
    
    for more info visit:  https://github.com/khalilrached/share-this
    
    if you have a issue or suggestion visit:  https://github.com/khalilrached/share-this/issues
    
```