const http = require("http");
const path = require("path");
const express = require("express");
const socketIo = require("socket.io");
const needle = require("needle");
const config = require("dotenv").config();
const TOKEN = process.env.TWITTER_BEARER_TOKEN;
const PORT = process.env.PORT || 5000;

const app = express();

const server = http.createServer(app);
const io = socketIo(server);

app.get("/", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../", "client", "index.html"));
});

const rulesURL = "https://api.twitter.com/2/tweets/search/stream/rules";
const streamURL =
  "https://api.twitter.com/2/tweets/search/stream?tweet.fields=public_metrics&expansions=author_id,geo.place_id";

const followersURL = "https://api.twitter.com/2/users/"; // + :id/followers;

const rules = [{ value: "coding" }];

// Get stream rules
async function getRules() {
  const response = await needle("get", rulesURL, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
    },
  });
  console.log(response.body);
  return response.body;
}

// Set stream rules
async function setRules() {
  const data = {
    add: rules,
  };

  const response = await needle("post", rulesURL, data, {
    headers: {
      "content-type": "application/json",
      Authorization: `Bearer ${TOKEN}`,
    },
  });
  console.log(response.body);
  return response.body;
}

// Delete stream rules
async function deleteRules(rules) {
  if (!Array.isArray(rules.data)) {
    return null;
  }

  const ids = rules.data.map((rule) => rule.id);

  const data = {
    delete: {
      ids: ids,
    },
  };

  const response = await needle("post", rulesURL, data, {
    headers: {
      "content-type": "application/json",
      Authorization: `Bearer ${TOKEN}`,
    },
  });

  return response.body;
}

function streamTweets(socket) {
  const stream = needle.get(streamURL, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
    },
  });

  //   console.log("stream", stream);

  stream.on("data", async (data) => {
    console.log(data);
    // console.log("Sadsd", data);
    try {
      const json = JSON.parse(data);

      // // if (i == 1) {
      // const response = await needle(
      //   "get",
      //   followersURL + json.data.author_id + "/followers",
      //   {
      //     headers: {
      //       Authorization: `Bearer ${TOKEN}`,
      //     },
      //   }
      // );
      // console.log("gfcgffh", response.body.data.length);
      // json.followerCount = response.body.data.length;
      // }
      // json.followerCount = respon
      // console.log(response.body);
      // console.log(json);
      // console.log();
      socket.emit("tweet", json);
    } catch (error) {
      console.log(error);
    }
  });

  return stream;
}

io.on("connection", async () => {
  //   console.log("Client connected...");
  console.log("Client connected...");

  let currentRules;

  try {
    //   Get all stream rules

    currentRules = await getRules();

    // Delete all stream rules
    await deleteRules(currentRules);

    // Set rules based on array above
    await setRules();
    // await getRules();
  } catch (error) {
    console.error(error);
    process.exit(1);
  }

  //   console.log("DFgdfg");
  streamTweets(io);
});

// (async () => {
//   console.log("Client connected...");

//   let currentRules;

//   try {
//     //   Get all stream rules
//     currentRules = await getRules();

//     // Delete all stream rules
//     await deleteRules(currentRules);

//     // Set rules based on array above
//     await setRules();
//     // await getRules();
//   } catch (error) {
//     console.error(error);
//     process.exit(1);
//   }
//   streamTweets();

//   // const filteredStream = streamTweets(io);

//   // let timeout = 0;
//   // filteredStream.on("timeout", () => {
//   //   // Reconnect on error
//   //   console.warn("A connection error occurred. Reconnecting…");
//   //   setTimeout(() => {
//   //     timeout++;
//   //     streamTweets(io);
//   //   }, 2 ** timeout);
//   //   streamTweets(io);
//   // });
// })();

server.listen(PORT, () => console.log(`Listening on port ${PORT}`));
