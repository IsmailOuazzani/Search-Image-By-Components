// Run object detection for all img folder if not already in database.json
// Run object detection for newly added images, add to database.json

const chokidar = require('chokidar');
const {spawn} = require('child_process');
const path = require('path');
const fs = require('fs');

// Initialize database.json
const absPath = path.join(__dirname, 'img');
fs.readdir(absPath, (err, files) => {
    // handling error
    if(err) {
        return console.log('Unable to load dirrectory: ' + err);
    }
    // prepare arguments for python command
    const command = ['handler.py', '-f', 'temp.txt'];
    // create text file containing images to analyze by python handler
    files.forEach((file) => {
        fs.appendFile('temp.txt', path.join('img',file + '\r\n'), (err) => {
            if (err) {
                console.log(err);
            }
        })
    });

    const py = spawn('python', command);
    // add to JSON database file
    py.stdout.on('data', (data) => {
        console.log(data.toString());
        database.push(JSON.parse(data.toString()));
        fs.writeFile('database.json', JSON.stringify(database), err => {
            if (err){
                console.log(err);
            };
        });
        
    });

    py.on('close', (code) => {
        console.log(`Initialized directory. Exited python with code: ${code}`);
    });
})


// Update database.json
const database = require('./database');
const dPath = 'img';
chokidar.watch(dPath, {ignoreInitial: true}) // ignore images already in database
    .on('add', (path) => {
        var command = [path];
        command.unshift('-c');
        command.unshift('handler.py');

        const py = spawn('python', command);
        // add to JSON database file
        py.stdout.on('data', (data) => {
            console.log(data.toString());
            database.push(JSON.parse(data.toString()));
            fs.writeFile('database.json', JSON.stringify(database), err => {
                if (err){
                    console.log(err);
                };
            });
           
        });

        py.on('close', (code) => {
            console.log(`Python exited with code ${code}`);
        });

    })
    .on('unlink', (path) => {
        console.log(`File ${path} has been removed`);
        // console.log(path.slice(4))
        // delete database[path.slice(4)]
        //     fs.writeFile('database.json', JSON.stringify(database), err => {
        //         if (err){
        //             console.log(err);
        //         };
        //     });
    })

// 