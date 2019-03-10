function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   J = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

up = ones(size(z));
g = up ./ (1.0 + exp(-1 * z));

% =============================================================

end
