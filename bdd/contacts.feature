Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | firstname  | lastname  | email  |
  | firstname1 | lastname1 | email1 |
  | firstname2 | lastname2 | email2 |

Scenario Outline: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact

Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname> and <email>
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list with the modified contact

  Examples:
  | firstname  | lastname  | email  |
  | firstname3 | lastname3 | email3 |
  | firstname4 | lastname4 | email4 |
