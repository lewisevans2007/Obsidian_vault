#web 

CSS (Cascading Style Sheets) is a styling language used to describe the presentation and appearance of [[HTML]] elements on a web page. It allows you to control various aspects of your web page's layout, colors, fonts, and more. Here's an overview of CSS and its key concepts:

## CSS Syntax

CSS consists of rules that define how [[HTML]] elements should be displayed. Each rule contains a selector and one or more declarations.

```css
selector {
  property: value;
  /* more properties and values */
}
```

- **Selector**: Specifies which HTML elements the rule applies to. For example, you can target all paragraphs with `p`, or a specific element with an ID like `#myElement`, or a class with `.myClass`.
- **Property**: Represents the aspect of the element you want to style, such as `color`, `font-size`, or `background`.
- **Value**: Specifies the value for the property. For example, `red` for `color`, `14px` for `font-size`, or `url(image.jpg)` for `background`.

## Applying CSS

There are three main ways to apply CSS to your HTML document:

1. **Inline CSS**: Apply styles directly to an HTML element using the `style` attribute.

   ```html
   <p style="color: blue;">This is a blue paragraph.</p>
   ```

2. **Internal CSS**: Place CSS rules within the `<style>` tags in the `<head>` section of your [[HTML]] document.

   ```html
   <head>
     <style>
       p {
         color: blue;
       }
     </style>
   </head>
   <body>
     <p>This is a blue paragraph.</p>
   </body>
   ```

3. **External CSS**: Create a separate CSS file and link it to your [[HTML]] document using the `<link>` tag.

   ```html
   <head>
     <link rel="stylesheet" href="styles.css">
   </head>
   ```

   In the `styles.css` file:

   ```css
   p {
     color: blue;
   }
   ```

## CSS Selectors

CSS offers various selectors to target specific [[HTML]] elements for styling. Here are some commonly used selectors:

- **Element selector**: Targets all instances of a specific [[HTML]] element.

  ```css
  p {
    /* styles for paragraphs */
  }
  ```

- **ID selector**: Targets a specific [[HTML]] element with a unique ID attribute.

  ```css
  #myElement {
    /* styles for the element with ID "myElement" */
  }
  ```

- **Class selector**: Targets [[HTML]] elements with a specific class attribute.

  ```css
  .myClass {
    /* styles for elements with class "myClass" */
  }
  ```

- **Attribute selector**: Targets [[HTML]] elements with a specific attribute.

  ```css
  input[type="text"] {
    /* styles for text input elements */
  }
  ```

- **Pseudo-classes and pseudo-elements**: Allows you to target elements in specific states or positions, such as `:hover` or `::before`.

  ```css
  a:hover {
    /* styles for link when hovered */
  }

  p::first-line {
    /* styles for the first line of a paragraph */
  }
  ```

## CSS Properties

CSS offers a wide range of properties to control the appearance of [[HTML]] elements. Here are some commonly used properties:

- **Color**: Sets the text color.

  ```css
  color: red;
  ```

- **Font**: Specifies the font family, size, weight, and style.

  ```css
  font-family: Arial, sans-serif;
  font-size: 16px;
  font-weight: bold;
  font-style: italic;
  ```

- **Background**: Defines the background color or image of an element.

  ```css
  background-color: lightblue;
  background-image: url(image.jpg);
  ```

- **Margin**: Controls the space around an element.

  ```css
  margin: 10px;
  margin-top: 10px;
  ```

- **Padding**: Sets the space between the content and the border of an element.

  ```css
  padding: 10px;
  padding-left: 10px;
  ```

- **Border**: Specifies the style, width, and color of an element's border.

  ```css
  border: 1px solid black;
  border-radius: 5px;
  ```

- **Width and Height**: Sets the dimensions of an element.

  ```css
  width: 200px;
  height: 100px;
  ```

These are just a few examples of CSS properties available for styling [[HTML]] elements. CSS offers a wide range of properties to control almost every aspect of element appearance.

## CSS Box Model

The CSS Box Model describes how elements are rendered and how their dimensions are calculated. It consists of four parts:

- **Content**: The actual content of the element, such as text or images.
- **Padding**: The space between the content and the element's border.
- **Border**: The line that surrounds the padding and content.
- **Margin**: The space between the border and neighboring elements.

Understanding the box model helps you control the size, spacing, and layout of elements on your web page.

## CSS Units

CSS provides various units for specifying lengths and sizes. Some commonly used units include:

- **Pixels (px)**: Absolute unit based on the screen pixel.
- **Percentage (%)**: Relative unit based on the parent element's size.
- **Em (em)**: Relative unit based on the element's font size.
- **Rem (rem)**: Relative unit based on the root element's font size.
- **Viewport Width (vw)**: Relative unit based on the viewport width.
- **Viewport Height (vh)**: Relative unit based on the viewport height.

Using appropriate units helps ensure your web page's responsiveness and adaptability to different screen sizes.

## CSS Selectors and Specificity

When multiple CSS rules target the same element, the specificity of the selectors determines which styles are applied. Specificity is based on the selector's type, class, ID, and inline styles. Understanding specificity helps you control the order and priority of style application.

## CSS Frameworks

CSS frameworks like [[Bootstrap]], [[Foundation]], and [[Bulma]] provide pre-designed CSS and [[HTML]] templates, making it easier to create responsive and visually appealing web pages. These frameworks offer a grid system, UI components, and pre-styled elements, saving development time and effort.

## Conclusion

CSS is a powerful tool for controlling the appearance of [[HTML]] elements on your web page. With CSS, you can apply styles, control layout, and create visually appealing designs. By understanding CSS syntax, selectors, properties, and units, you can effectively style your HTML content and create engaging web experiences.