'use strict';

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _reactDom = require('react-dom');


var _reactDom2 = _interopRequireDefault(_reactDom);

var _autocomplete = require('react-toolbox/lib/autocomplete');

var _autocomplete2 = _interopRequireDefault(_autocomplete);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

alert("react");

var ContactItem = _react2.default.createClass({
  displayName: 'ContactItem',

  propTypes: {
    name: _react2.default.PropTypes.string.isRequired,
    email: _react2.default.PropTypes.string.isRequired,
    description: _react2.default.PropTypes.string
  },

  render: function render() {
    return _react2.default.createElement('li', { className: 'ContactItem' }, _react2.default.createElement('h2', { className: 'ContactItem-name' }, this.props.name), _react2.default.createElement('a', { className: 'ContactItem-email', href: 'mailto:' + this.props.email }, this.props.email), _react2.default.createElement('div', { className: 'ContactItem-description' }, this.props.description));
  }
});

var ContactForm = _react2.default.createClass({
  displayName: 'ContactForm',

  propTypes: {
    value: _react2.default.PropTypes.object.isRequired,
    onChange: _react2.default.PropTypes.func.isRequired
  },

  render: function render() {
    var oldContact = this.props.value;
    var _onChange = this.props.onChange;

    return _react2.default.createElement('form', { className: 'ContactForm' }, _react2.default.createElement('input', {
      type: 'text',
      placeholder: 'Name (required)',
      value: this.props.value.name,
      onChange: function onChange(e) {
        _onChange(Object.assign({}, oldContact, { name: e.target.value }));
      }
    }), _react2.default.createElement('input', {
      type: 'email',
      placeholder: 'Email (required)',
      value: this.props.value.email,
      onChange: function onChange(e) {
        _onChange(Object.assign({}, oldContact, { email: e.target.value }));
      }
    }), _react2.default.createElement('textarea', {
      placeholder: 'Description',
      value: this.props.value.description,
      onChange: function onChange(e) {
        _onChange(Object.assign({}, oldContact, { description: e.target.value }));
      }
    }), _react2.default.createElement('button', { type: 'submit' }, "Add Contact"));
  }
});

var ContactView = _react2.default.createClass({
  displayName: 'ContactView',

  propTypes: {
    contacts: _react2.default.PropTypes.array.isRequired,
    newContact: _react2.default.PropTypes.object.isRequired,
    onNewContactChange: _react2.default.PropTypes.func.isRequired
  },

  render: function render() {
    var contactItemElements = this.props.contacts.filter(function (contact) {
      return contact.email;
    }).map(function (contact) {
      return _react2.default.createElement(ContactItem, contact);
    });

    return _react2.default.createElement('div', { className: 'ContactView' }, _react2.default.createElement('h1', { className: 'ContactView-title' }, "Contacts"), _react2.default.createElement('ul', { className: 'ContactView-list' }, contactItemElements), _react2.default.createElement(ContactForm, {
      value: this.props.newContact,
      onChange: this.props.onNewContactChange
    }));
  }
});

/*
 * Actions
 */

function updateNewContact(contact) {
  setState({ newContact: contact });
}

/*
 * Model
 */

// The app's complete current state
var state = {};

// Make the given changes to the state and perform any required housekeeping
function setState(changes) {
  Object.assign(state, changes);

  _reactDom2.default.render(_react2.default.createElement(ContactView, Object.assign({}, state, {
    onNewContactChange: updateNewContact
  })), document.getElementById('share-recipe-form'));
}

// Set initial data
setState({
  contacts: [{ key: 1, name: "James K Nelson", email: "james@jamesknelson.com", description: "Front-end Unicorn" }, { key: 2, name: "Jim", email: "jim@example.com" }],
  newContact: { name: "", email: "", description: "" }
});