# PttData

Get ptt user's info and post

change .env.example to .env and enter 
```
ptt_acc={ptt acount}
ptt_pswd={ptt password}
```
then
```
 pip install -r requirements.txt
    
 python app.py
```

## Api

### get user info

http://127.0.0.1:5000/user/{ptt_id}

### get user 5 post within 7 days

http://127.0.0.1:5000/post/{ptt_id}

## Example

https://pttdata.herokuapp.com/user/ptt

https://pttdata.herokuapp.com/post/ptt
