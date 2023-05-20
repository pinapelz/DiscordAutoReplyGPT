/**
 * @name WebSocketChatRelayer
 * @author Pinapelz
 * @description A helper plugin for relaying messages from Discord through a WebSocket to a server.
 * @version 0.0.1
 */


const { Webpack } = BdApi;
const { Filters } = Webpack;
const Dispatcher = Webpack.getModule(Filters.byProps("isDispatching", "subscribe"));
const socket = new WebSocket('ws://localhost:8765');

socket.onopen = function () {
  console.log('WebSocket connection established.');
};

socket.onclose = function (event) {
  console.log('WebSocket connection closed:', event.code, event.reason);
};

module.exports = meta => ({
  onMessage: ({message, channelId}) => {
    if (message["author"]["id"] == 226550337417379850) {
      console.log(channelId);
      if (socket.readyState === WebSocket.OPEN) {
        console.log(message)
        socket.send(message["content"]);
      }
    }
  },

  start() {
    Dispatcher.subscribe('MESSAGE_CREATE', this.onMessage);
  },

  stop() {
    Dispatcher.unsubscribe('MESSAGE_CREATE', this.onMessage);
  }
});
