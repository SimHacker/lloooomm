# Project Plan: Character Bookshelves

## 1. Overview

The "Character Bookshelves" project aims to create curated collections of books associated with influential figures, both real and fictional. These bookshelves will serve as a way to explore the intellectual and inspirational worlds of these characters, providing insight into their work and ideas. The collections will be a resource for discovery, helping users find new and interesting books, and will be integrated into the lloooomm ecosystem.

The core principles are:
- **Diversity:** Represent a wide range of voices, disciplines, and perspectives.
- **Inspiration:** The lists should be inspiring, not just comprehensive. It's okay to be creative and thematic.
- **Representation:** Include books *by* the character, books that influenced them, and books *about* them (such as biographies and critical analyses) to provide a holistic view.
- **Flexibility:** The data model for books should accommodate various sources, including the Internet Archive, commercial sites like Amazon, and other URLs.
- **Interconnectivity:** Bookshelves should connect to the broader lloooomm knowledge base.

## 2. Phase 1: The Pioneers

We will start by creating bookshelves for two foundational figures in computing.

### 2.1. Brett Victor's Bookshelf

Sourced from his "five-star list" of highly recommended works. This list is a treasure trove of design, engineering, and societal thinking.

**Design**
- *The Visual Display of Quantitative Information* – Edward R. Tufte
- *Envisioning Information* – Edward R. Tufte
- *Beautiful Evidence* – Edward R. Tufte
- *Meggs' History of Graphic Design* – Phillip B. Meggs & Alston W. Purvis
- *The Elements of Graphing Data* – William S. Cleveland
- *Logic & Design* – Krome Barratt
- ★ *Understanding Comics: The Invisible Art* – Scott McCloud
- *Reinventing Comics: How Imagination and Technology Are Revolutionizing an Art Form* – Scott McCloud
- *Making Comics: Storytelling Secrets of Comics, Manga, and Graphic Novels* – Scott McCloud
- *The Design of Everyday Things* – Donald Norman
- *Designing for People* – Henry Dreyfuss
- ★ *Cradle to Cradle* – Michael Braungart & William McDonough
- ★ *The Inmates are Running the Asylum* – Alan Cooper
- *About Face 2.0* – Alan Cooper
- *The Humane Interface* – Jef Raskin
- *Rules of Play: Game Design Fundamentals* – Katie Salen Tekinbas & Eric Zimmerman
- *A Theory of Fun* – Raph Koster

**Engineering**
- *Structure and Interpretation of Computer Programs* – Harold Abelson & Gerald Jay Sussman
- *The Little Schemer* – Daniel P. Friedman, Matthias Felleisen, Duane Bibby, and Gerald J. Sussman
- *Hacker's Delight* – Henry Warren, Jr.
- *The Design and Evolution of C++* – Bjarne Stroustrup
- *Reforming the Mathematical Language of Physics* – David Hestenes
- *Nonlinear Dynamics and Chaos* – Steven Strogatz
- *Visual Complex Analysis* – Tristan Needham
- *Gödel, Escher, Bach* – Douglas Hofstadter
- ★★ *The Art of Doing Science and Engineering* – Richard Hamming
- *And Suddenly the Inventor Appeared* – Genrich Altshuller
- *Folklore* – Andy Hertzfeld

**Society**
- ★★ *Mindstorms* – Seymour Papert
- *Dumbing Us Down* – John Taylor Gatto
- *How Children Fail* – John Holt
- *How to Survive in your Native Land* – James Herndon
- *Technopoly* – Neil Postman
- *The Structure of Scientific Revolutions* – Thomas Kuhn
- *Guns, Germs, and Steel* – Jared Diamond
- *Amusing Ourselves to Death* – Neil Postman
- ★ *The Corporation* – Joel Balkan, et al.
- *A People's History of the United States* – Howard Zinn
- *Lies My Teacher Told Me* – James Loewen

### 2.2. Alan Kay's Bookshelf

Sourced from his own recommendations for computer science students. This list focuses on foundational texts that expand thinking about computation.

- *Lisp 1.5 Programmers Manual* – John McCarthy
- *Computation: Finite and Infinite Machines* – Marvin Minsky
- *Advances in Programming and Non-Numerical Computation* – Ed. L. Fox
- *The Mythical Man-Month* – Fred Brooks
- *The Sciences of the Artificial* – Herb Simon
- *A Programming Language* – Ken Iverson
- *Control Structures for Programming Languages* – Dave Fisher
- *The Art of the Metaobject Protocol* – Gregor Kiczales, et al.
- *Making Erlang* (Joe Armstrong's PhD thesis) – Joe Armstrong

## 3. Phase 2: Expanding the Library

To ensure diversity, we will create bookshelves for a range of thinkers. Here are some proposed characters and themes:

*   **Ada Lovelace:** *The Enchantress of Numbers.* Books on early mathematics (Babbage, De Morgan), industrial machinery, Romantic poetry (Byron), and key biographies that illuminate her life and contributions.
*   **Octavia Butler:** *Parables and Possibilities.* Books on afrofuturism, biology, genetics, social justice, and classic science fiction that shaped her work.
*   **Grace Hopper:** *The Admiral's Library.* Books on COBOL, early computing history, naval strategy, and leadership.
*   **Jorge Luis Borges:** *The Library of Babel.* A collection of metaphysical philosophy, paradoxical tales, detective stories, and foundational texts of fantasy literature.
*   **Ursula K. Le Guin:** *The Dispossessed's Collection.* Works on anarchism, Taoism, feminism, cultural anthropology, and the fantasy and sci-fi that inspired her.
*   **Donella Meadows:** *The Systems Thinker's Shelf.* Books on cybernetics, environmental science, sustainability, and of course, her own seminal work "Thinking in Systems".
*   **bell hooks:** *A Shelf for Transgression.* Foundational texts on critical theory, feminism, race, class, and education.
*   **Philip K. Dick:** *Do Androids Dream of an Electric Bookshelf?* Works on gnosticism, metaphysics, philosophy of mind, paranoia, and the nature of reality, alongside his own influential novels.
- **Brad Myers:** *The Interactionist's Desk.* Featuring his own "Pick, Click, Flick!" and other key works in Human-Computer Interaction and Programming by Demonstration.

## 4. Data Model and Implementation

We will use YAML to represent the data for its support for comments and overall readability.

### Book Data Structure

Each book should have a flexible data structure that can accommodate various links and metadata.

```yaml
- title: "Title of the Book"
  author: "Author Name"
  year: 1984
  # A review or quote from the bookshelf's owner. Can be multi-line.
  review: >
    A short review or a quote from the bookshelf's owner.
  rating: 5 # Optional rating (1-5 stars)
  links:
    internet_archive: "url_to_internet_archive_scan"
    amazon: "url_to_amazon_page"
    project_gutenberg: "url_to_gutenberg_text"
    more_info: "url_to_wikipedia_or_author_page"
  tags:
    - science_fiction
    - dystopian
    - philosophy
```

### Bookshelf Collection

A bookshelf will be a collection of these book objects, associated with a character, and stored in a single YAML file.

```yaml
# Filename: alan-kay-bookshelf.yml
character: "Alan Kay"
theme: "Foundations of Computation"
books:
  - title: "Lisp 1.5 Programmers Manual"
    author: "John McCarthy"
    # ... more book properties
  - title: "Computation: Finite and Infinite Machines"
    author: "Marvin Minsky"
    # ... more book properties
```

### Implementation Steps

1.  **Schema Definition:** Formalize the YAML schemas for `Book` and `Bookshelf` collections.
2.  **Data Ingestion:** Create scripts to slurp the initial book lists for Brett Victor and Alan Kay into YAML files. We can start by searching the Internet Archive and other sources for the links.
3.  **Curation and Creation:** Begin curating the proposed diverse bookshelves. This can be a collaborative process.
4.  **Frontend Component:** Design and build a Svelte component to display a "bookshelf" attractively.
5.  **Integration:** Integrate the bookshelves into character pages and other relevant parts of the lloooomm.

This plan should give us a solid foundation to build upon. Let's start weaving these new threads into our cosmic library! 