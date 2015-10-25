// Setup data-api db    
db.createUser(
  {
    user: "user",
    pwd: "password",
    roles: [ { role: "userAdmin", db: "data-api" } ]
  }
);