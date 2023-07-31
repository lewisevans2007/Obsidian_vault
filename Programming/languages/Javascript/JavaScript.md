#web 

JavaScript is a programming language that adds interactivity and dynamic behaviour to web pages. It can manipulate and modify [[HTML]] elements, apply [[CSS]] styles, and respond to user actions. Here's an overview of how JavaScript can interact with [[HTML]] and [[CSS]]:

## Accessing HTML Elements

JavaScript provides several methods to access and manipulate [[HTML]] elements within your web page. The most commonly used methods include:

- **getElementById**: Retrieves an element using its unique ID.

  ```javascript
  const element = document.getElementById('myElement');
  ```

- **getElementsByClassName**: Returns a collection of elements with a specific class.

  ```javascript
  const elements = document.getElementsByClassName('myClass');
  ```

- **getElementsByTagName**: Retrieves elements based on the tag name.

  ```javascript
  const elements = document.getElementsByTagName('p');
  ```

- **querySelector**: Returns the first element that matches a specific [[CSS]] selector.

  ```javascript
  const element = document.querySelector('#myElement');
  ```

- **querySelectorAll**: Returns a NodeList containing all elements that match a specific [[CSS]] selector.

  ```javascript
  const elements = document.querySelectorAll('.myClass');
  ```

Once you have selected an element, you can manipulate its properties, change its content, apply [[CSS]] styles, or attach event listeners.

## Modifying HTML Content

JavaScript allows you to manipulate the content of [[HTML]] elements. You can change the text, update attributes, add or remove elements, and more. Here are a few examples:

- **Changing text content**:

  ```javascript
  const element = document.getElementById('myElement');
  element.textContent = 'New text content';
  ```

- **Modifying attributes**:

  ```javascript
  const image = document.getElementById('myImage');
  image.src = 'new-image.jpg';
  ```

- **Creating and appending elements**:

  ```javascript
  const list = document.getElementById('myList');
  const listItem = document.createElement('li');
  listItem.textContent = 'New item';
  list.appendChild(listItem);
  ```

## Applying CSS Styles

JavaScript can modify and apply [[CSS]] styles to [[HTML]] elements. You can add, remove, or toggle [[CSS]] classes, change individual style properties, or directly modify inline styles. Here are some examples:

- **Adding and removing classes**:

  ```javascript
  const element = document.getElementById('myElement');
  element.classList.add('newClass');
  element.classList.remove('oldClass');
  ```

- **Changing style properties**:

  ```javascript
  const element = document.getElementById('myElement');
  element.style.backgroundColor = 'blue';
  element.style.fontSize = '20px';
  ```

- **Modifying inline styles**:

  ```javascript
  const element = document.getElementById('myElement');
  element.style.cssText = 'background-color: blue; font-size: 20px;';
  ```

## Handling Events

JavaScript allows you to respond to user actions, such as clicks, mouse movements, or form submissions, by attaching event listeners to [[HTML]] elements. Event listeners execute a specific function when the event occurs. Here's an example:

```javascript
const button = document.getElementById('myButton');

button.addEventListener('click', function() {
  // Code to be executed when the button is clicked
});
```

You can attach event listeners to various HTML elements and perform actions based on user interactions.