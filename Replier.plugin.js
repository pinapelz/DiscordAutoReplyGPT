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
  // Both values can be retrieved by right clicking on a channel or user and selecting "Copy ID" after turning on Developer Mode in Discord settings
  let listenChannelId = 1; // Channel ID you want to listen to
  let selfUserId = 1; // Your User ID (Ensure your own messages aren't broadcasted)

  const updateUserId = (value) => {
    listenChannelId = value;
  };

  const updateSelfUserid = (value) => {
    selfUserId = value;
  };

  return {
    onMessage: ({message, channelId}) => {
      if (message["author"]["id"] != selfUserId && channelId == listenChannelId) {
        console.log(listenChannelId);
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

        // Cahnnel ID input field
        const userIdContainer = document.createElement('div');
        const userIdLabel = document.createElement('label');
        userIdLabel.textContent = 'Channel ID:';
        userIdContainer.appendChild(userIdLabel);
        const userIdInput = document.createElement('input');
        userIdInput.type = 'text';
        userIdInput.placeholder = 'Enter Channel ID';
        userIdInput.value = listenChannelId;
        userIdInput.addEventListener('input', (event) => {
          updateUserId(event.target.value);
        });
        userIdContainer.appendChild(userIdInput);
        panel.appendChild(userIdContainer);

        // Self User ID input field
        const selfUserIdContainer = document.createElement('div');
        const selfUserIdLabel = document.createElement('label');
        selfUserIdLabel.textContent = 'Self User ID:';
        selfUserIdContainer.appendChild(selfUserIdLabel);
        const selfUserIdInput = document.createElement('input');
        selfUserIdInput.type = 'text';
        selfUserIdInput.placeholder = 'Enter Self User ID';
        selfUserIdInput.value = selfUserId;
        selfUserIdInput.addEventListener('input', (event) => {
          updateSelfUserid(event.target.value);
        });
        selfUserIdContainer.appendChild(selfUserIdInput);
        panel.appendChild(selfUserIdContainer);

        // Save button
        const saveButton = document.createElement('button');
        saveButton.textContent = 'Save';
        saveButton.addEventListener('click', () => {
          socket = new WebSocket('ws://localhost:8765');
          BdApi.saveData(meta.name, 'userId', listenChannelId);
        });
        panel.appendChild(saveButton);

        return panel;
      }
      };
    


};