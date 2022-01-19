const express = require('express')
const app = express()
const port = 3000
app.use(express.static('/'));

app.get('/', (req, res) => {
  res.sendFile("D:/xampp/htdocs/html-gateway/index.html")
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})