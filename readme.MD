# LazyStarter
LazyStarter is a composable, component-based scaffolding framework.

- **Extensible**: Add your own components and templates.
- **Language-Agnostic:** Templates can be in your programming language of your choice
- **Do It Once, Get It Twice:** Write your components and we take care of creating the flags for you!
- **Component-Based**
- **

# Usage
link image here

### Glossary

Bases: A Base is the minimum skeleton of buildable templates.
Default bases include (landing-page, portfolio-page)

Components: components are children of Bases. A Component must be a child of at least one Base.
Components are invoked via --flags.
Default components include (navbar, navbar-searchbar, sidebar, footer, footer-big, --background-video)