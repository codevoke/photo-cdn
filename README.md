# photo-cdn
simple photo cdn (python flask)

cdn crud system:

> create:  
> `POST:   /create         - upload photo (input: file 'photo', output: file id)`  
read:  
> `GET:    /{file id}.png  - read   photo`  
update:  
> `PUT:    /{file id}      - update photo (input: file 'photo')`  
delete:  
> `DELETE: /{file id}      - delete photo`  
