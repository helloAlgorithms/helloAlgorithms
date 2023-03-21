#include <algorithm>
#include <deque>
#include <iostream>

struct Student {
  int id;
  int postedOrder;
  int voteCount;

  Student(int id, int postedOrder, int voteCount)
      : id(id), postedOrder(postedOrder), voteCount(voteCount) {
  }
};

struct Cmp1 {
  bool operator()(const Student& a, const Student& b) {
    if (a.voteCount == b.voteCount)
      return (a.postedOrder < b.postedOrder);
    return (a.voteCount < b.voteCount);
  }
};

struct Cmp2 {
  bool operator()(const Student& a, const Student& b) {
    return (a.id < b.id);
  }
};

struct StudentQue {
  std::size_t maxSize;
  std::deque<Student> arr;
  int postCount;

  StudentQue(const int size) : maxSize(size), arr(), postCount() {
  }

  void removeOne(void) {
    std::sort(this->arr.begin(), this->arr.end(), Cmp1());
    this->arr.pop_front();
  }

  void insert(const int id) {
    for (std::deque<Student>::iterator it = this->arr.begin();
         it != this->arr.end();
         ++it) {
      if (it->id == id) {
        ++it->voteCount;
        return;
      }
    }
    if (this->arr.size() >= maxSize) {
      this->removeOne();
    }
    this->arr.push_back(Student(id, postCount, 1));
    ++this->postCount;
  }
};

std::ostream& operator<<(std::ostream& os, StudentQue& q) {
  std::sort(q.arr.begin(), q.arr.end(), Cmp2());

  for (std::deque<Student>::iterator it = q.arr.begin(); it != q.arr.end();
       ++it) {
    os << it->id << " ";
  }
  return (os);
}

int main(void) {
  int n, m, tmp;
  std::cin >> n >> m;
  StudentQue q(n);
  for (int i = 0; i < m; ++i) {
    std::cin >> tmp;
    q.insert(tmp);
  }
  std::cout << q << std::endl;
  return (0);
}
