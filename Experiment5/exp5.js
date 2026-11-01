use store;

db.products.insertMany([
    { "name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50, "rating": 4.5 },
    { "name": "Mouse", "category": "Electronics", "price": 25, "stock": 200, "rating": 4.0 },
    { "name": "Keyboard", "category": "Electronics", "price": 75, "stock": 150, "rating": 4.2 },
    { "name": "Desk Chair", "category": "Furniture", "price": 150, "stock": 75, "rating": 4.8 },
    { "name": "Monitor", "category": "Electronics", "price": 300, "stock": 100, "rating": 4.7 },
    { "name": "Coffee Table", "category": "Furniture", "price": 100, "stock": 40, "rating": 3.9 },
    { "name": "External HDD", "category": "Storage", "price": 80, "stock": 120, "rating": 4.1 },
    { "name": "Webcam", "category": "Electronics", "price": 60, "stock": 90, "rating": 4.6 }
]);

db.products.countDocuments({});
db.products.countDocuments({ "category": "Electronics" });

db.products.find().sort({ "price": 1 });
db.products.find({ "category": "Electronics" }).sort({ "rating": -1});

db.products.find().sort({ "price": -1}).limit(3);
db.products.find().sort({ "name": 1 }).skip(2).limit(3);

db.products.aggregate([
    {
        $group: {
            _id: "$category",
            averagePrice: { $avg: "$price" },
            totalStock: { $sum: "$stock" }
        }
    },
    {
        $sort: { "averagePrice":-1}
    }
]);
