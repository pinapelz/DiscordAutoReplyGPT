/**
 * @name AutoReplier
 * @author Pinapelz
 * @description Something goes here. But idk what yet
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



module.exports = meta => {
  let userId = 232146633830170624;

  const updateUserId = (value) => {
    userId = value;
  };

  return {
    onMessage: ({message, channelId}) => {
      if (message["author"]["id"] == userId) {
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
    },

    getSettingsPanel: () => {
      const panel = document.createElement('div');
      const input = document.createElement('input');
      input.type = 'text';
      input.placeholder = 'Enter User ID';
      input.value = userId;
      input.addEventListener('input', (event) => {
        updateUserId(event.target.value);
      });
      panel.appendChild(input);

      const saveButton = document.createElement('button');
      saveButton.textContent = 'Save';
      saveButton.addEventListener('click', () => {
        BdApi.saveData(meta.name, 'userId', userId);
      });
      panel.appendChild(saveButton);

      return panel;
    }
  };
};