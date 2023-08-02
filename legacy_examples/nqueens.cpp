#include <iostream>
#include <vector>

using namespace std;

bool isSafe(vector<vector<char>>& board, int row, int col, int N) {
    // Check for queens in the same column
    for (int i = 0; i < row; ++i) {
        if (board[i][col] == 'Q') {
            return false;
        }
    }

    // Check upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; --i, --j) {
        if (board[i][j] == 'Q') {
            return false;
        }
    }

    // Check upper right diagonal
    for (int i = row, j = col; i >= 0 && j < N; --i, ++j) {
        if (board[i][j] == 'Q') {
            return false;
        }
    }

    return true;
}

void solveNQueens(vector<vector<char>>& board, int row, int N) {
    if (row == N) {
        // Print the solution
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cout << board[i][j] << ' ';
            }
            cout << endl;
        }
        cout << endl;
        return;
    }

    for (int col = 0; col < N; ++col) {
        if (isSafe(board, row, col, N)) {
            board[row][col] = 'Q';
            solveNQueens(board, row + 1, N);
            board[row][col] = '*';  // Backtrack
        }
    }
}

void printNQueens(int N) {
    vector<vector<char>> board(N, vector<char>(N, '*'));
    solveNQueens(board, 0, N);
}

int main() {
    int N;
    cout << "Enter the size of the chessboard (N): ";
    cin >> N;

    printNQueens(N);

    return 0;
}
