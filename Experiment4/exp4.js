db.student.insert({ 
    regNo: "3014",
    name: "Test Student",
    course: { courseName: "MCA", duration: "3 Years" }, 
    address: { city: "Bangalore", state: "KA", country: "India" } 
});

db.student.find();
db.student.find({"regNo":"3014"});

db.student.update({ "regNo": "3014" }, { $set: { "name": "Viraj" } });
db.student.remove({"regNo":"3014"});

var NEW_POST = {
    name: "Working with Arrays", 
    user: "Database Rebel",
    desc: "Maintaining an array of objects in a document",
    content: "some content...",
    created: new Date(),
    updated: new Date(),
    tags: [ "mongodb", "arrays"]
};
db.posts.insertOne(NEW_POST);

var NEW_COMMENT = {
    user: "DB Learner",
    text: "Nice post, can I know more about the arrays in MongoDB?",
    updated: new Date()
};
db.posts.updateOne(
    {_id: ObjectId("5ec55af811ac5e2e2aafb2b9") },
    { $push: { comments: NEW_COMMENT } }
);

db.posts.updateOne(
    {_id : ObjectId("5ec55af811ac5e2e2aafb2b9"), "comments.user": "Database Rebel" },
    {$set: {"comments.$.text": "Thank you, please look for updates - updated" } }
);

db.posts.updateOne(
    {_id: ObjectId("5ec55af811ac5e2e2aafb2b9") },
    { $pull: { comments: { user: "Database Rebel"}}}
);

db.posts.updateOne(
    {_id: ObjectId("5ec55af811ac5e2e2aafb2b9") },
    { $set: {"comments.$[].likes":0}}
);

db.posts.updateOne(
    {"_id" : ObjectId("5ec55af811ac5e2e2aafb2b9") },
    {$inc: {"comments.$[ele].likes": 1 } },
    {arrayFilters: [ { "ele.user": "DB Learner", "ele.likes": { $exists: false }}]}
);
