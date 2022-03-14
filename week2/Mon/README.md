문제 링크: https://leetcode.com/problems/find-peak-element/


## 문제

배열 내 peak element를 찾는 문제. peak element란 이웃한 다른 두 원소보다 strictly greater한 원소를 의미한다. 만약 여러개의 peak element가 있다면, 그 중 어떤 index를 반환해도 상관 없다.

**조건**
* 양 끝에 음의 무한대가 있다고 가정한다.
* 1 <= nums.length <= 1000
* -2\*\*31 <= nums[i] <= 2\*\*31 - 1
* nums[i] != nums[i + 1] for all valid i
* O(logn) 시간 복잡도로 해결하라.


## 페어프로그래밍을 통한 해결 방식
1. 선형 탐색으로는 쉽게 해결할 수 있을 것 같은데, O(logn)으로 해결하는 방법을 쉽게 떠올리지 못했다.
2. Related Topics에서 `binary search` 키워드를 보고, 이진 탐색으로 접근해보기로 결정
3. 주어진 `nums` 배열 양끝에 가장 작은 수를 추가한 후, 이진 탐색으로 peak 찾는 코드 작성
4. 연속하는 두 원소는 같지 않다는 조건이 주어졌고 양쪽에는 무한히 작은 값이 존재하기 때문에, 현재 중간값이 peak가 아닐 경우 양쪽으로 중간값을 이동하면서 탐색하면 반드시 peak가 나오게 되어있다. 


