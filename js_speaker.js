const zmq = require("zeromq");

const sock = new zmq.Request();
sock.connect("tcp://127.0.0.1:3000");

// Send a request message
sock.send("Quien eres tu?"); 

// Configurar un tiempo de espera (por ejemplo, 10 segundos)
const timeoutMilliseconds = 10000; // 10 segundos

// Crear una promesa para manejar la recepción con tiempo de espera
const receivePromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject(new Error("Timeout: No se recibió respuesta a tiempo"));
  }, timeoutMilliseconds);

  sock.receive()
    .then((msg) => {
      const reply = msg.toString();
      console.log("Received: %s", reply);
      resolve(reply);
    })
    .catch((error) => {
      reject(error);
    });
});

// Usar la promesa con tiempo de espera
receivePromise
  .then((reply) => {
    // Handle the reply here, e.g., use it in your application
    // You can access the reply message in the 'reply' variable
  })
  .catch((error) => {
    console.error("An error occurred:", error);
    // Handle the error here, e.g., retry or gracefully exit
  });
