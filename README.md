# 'support 2' task implementation.
### Content/Instruments:
Email sending, authorization (jwt token), celery, redis, docker
### Usage:
For authorization use JSON like this:
```
{
    "user": {
        "username": "user1",
        "email": "user1@user.user",
        "password": "qweasdzxc"
    }
}
```