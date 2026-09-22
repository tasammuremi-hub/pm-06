CREATE DATABASE MoviesReviewDB;
go
USE MoviesReviewDB;
go
CREATE TABLE MoviesReviewDB(
    ReviewID INT PRIMARY KEY IDENTITY (1,1)1,
    ReviewerName NVARCHAR(255) NOT NULL,
    MovieTitle NVARCHAR(255) NOT NULL,
    ReviewText NVARCHAR(255) NOT NULL,
    Rating INT NOT NULL
);
GO
