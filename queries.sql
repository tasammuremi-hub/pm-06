SELECT * FROM MoviesReviews;

SELECT* from MoviesReviews WHERE MovieTitle = 'The last Horizon';

SELECT * FROM MoviesReviews WHERE Ratings >=8;

UPDATE MoviesReviews SET Rating =9 WHERE ReviewID =1;

DELETE FROM MoviesReviews WHERE ReviewerName = 'Thabo Dlamini';
