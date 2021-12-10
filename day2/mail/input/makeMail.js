var fs = require('fs');

function randomStr(length) {
    return [...Array(length)].map(() => Math.random().toString(36)[2]).join('')
}

async function writeFile(fileName, content) {
    await fs.appendFileSync(fileName, `${content}\n`, function(err) {
        if (err) throw err;
        console.log('Updated!');
    });
}

function getRandomType() {
    const mails = ['gmail', 'yahoo', 'hotmail', 'outlook', 'mediafate', 'example'];

    const random = Math.floor(Math.random() * mails.length);
    return mails[random]
}

function generateMail() {
    let name = randomStr(20)
    let type = getRandomType()
    let password = randomStr(8)
    return `${name}@${type}.com:${password}`
}


async function makeMail(fileName, numberMail) {
    for (let i = 1; i <= numberMail; i++) {
        let mail = generateMail()
        await writeFile(fileName, i + mail)
    }
}

makeMail('mail3.txt', 400)
console.log('done');