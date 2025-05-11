# Arkkitehtuurikuvaus
## Rakenne
Sovelluksen rakenne koostuu editorin toiminnallisuuksista, tiedostojen käsittelystä, ja käyttöliittymästä vastaavista komponenteista.

## Sovelluslogiikka

Sovelluksen logiikka kohdentuu tiedostojen käsittelyyn, josta vastaa luokat FileHandler ja FileDatabase. FileDatabase vastaa myös tietokannasta, jota käsitellään käyttöliittymän kautta.

```mermaid
    classDiagram
    FileHandler "1" -- "1" FileDatabase
    class FileDatabase {
        conn
        .setup
        .add
        .remove
        .get
        .reset
    }
    class FileHandler {
        root
        textarea
        current_file
        database
    }
```

## Käyttöliittymä

Käyttöliittymästä vastaavat luokat UI, EditorMain, VisualEditor, ja SourceEditor.

### Tiedoston avaaminen

Alla oleva sekvenssikaavio kuvaa sitä, miten tiedoston tallentaminen onnistuu käyttöliittymästä:

```mermaid
    sequenceDiagram
    actor User
    participant UI
    participant FileHandler
    participant FileDatabase
    User->>UI: "Save" button
    UI->>FileHandler: save_file(file)
    FileHandler->>FileHandler: write()
    FileHandler->>FileDatabase: add_file(file_name, ...)
    FileDatabase->>FileDatabase: cursor.execute(sql)
    FileDatabase->>FileHandler: 
    FileHandler->>UI: messagebox.showinfo("Success", "File saved.")
```