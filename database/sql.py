'''
CREATE TABLE User
(
  UserID INT NOT NULL,
  UserName INT NOT NULL,
  UserPassword INT NOT NULL,
  OpenAIKey INT NOT NULL,
  PRIMARY KEY (UserID)
);

CREATE TABLE Session
(
  SessionID INT NOT NULL,
  SessionDate INT NOT NULL,
  Book INT NOT NULL,
  ShareLink INT NOT NULL,
  UserID INT NOT NULL,
  PRIMARY KEY (SessionID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);

CREATE TABLE Book
(
  BookID INT NOT NULL,
  AuthorName INT NOT NULL,
  ChapterID INT NOT NULL,
  BookTitle INT NOT NULL,
  BookDescription INT NOT NULL,
  BookCreationDate INT NOT NULL,
  ShareLink INT NOT NULL,
  SessionID INT NOT NULL,
  PRIMARY KEY (BookID),
  FOREIGN KEY (SessionID) REFERENCES Session(SessionID)
);

CREATE TABLE Chapter
(
  ChapterID INT NOT NULL,
  ChapterHeader INT NOT NULL,
  ChapterText INT NOT NULL,
  ChapterComments INT NOT NULL,
  BookID INT NOT NULL,
  UserID INT NOT NULL,
  PRIMARY KEY (ChapterID),
  FOREIGN KEY (BookID) REFERENCES Book(BookID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
);
'''
