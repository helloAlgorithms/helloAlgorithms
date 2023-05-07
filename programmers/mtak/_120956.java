/**
 * _120956
 */
public class _120956 {
	private boolean isBabComposedOfOngal(String bab) {
		String[] ongals = { "aya", "ye", "woo", "ma" };
		// 첫 글자부터 도장깨기
		int pIdx = 0;
		while (pIdx < bab.length()) {
			int startIdx = pIdx;
			for (String ongal : ongals) {
				if (bab.indexOf(ongal, startIdx) == startIdx) {
					pIdx += ongal.length();
					break;
				}
			}
			if (startIdx == pIdx)
				return false;
		}
		return true;
	}

	public int solution(String[] babbling) {
		int answer = 0;
		for (String bab : babbling) {
			if (isBabComposedOfOngal(bab))
				answer += 1;
		}
		return answer;
	}
	public static void main(String[] args) {
		_120956 sol = new _120956();
		int ret = sol.solution(new String[]{"aya", "yee", "u", "maa", "wyeoo"});
		System.out.print(ret);
		int ret1 = sol.solution(new String[]{"ayaye", "uuuma", "ye", "yemawoo", "ayaa"});
		System.out.print(ret1);
	}
}
// s1. 어떤 단서를 보고 무엇을 생각했나?
// 샘플 옹알이에 옹알이 재료가 한번씩만 들어감 => 옹알이 재료 중 같은 단어로 시작하는게 있다면 백트래킹으로 해야 할 듯.
// java 범위 슬라이싱 => substring(start, end)
// s2. 알아야 하는 개념과 적용 방법
// substring(), 
// s3. 단서-개념-적용
// 일정 범위 안 단어 찾기 => substring().equals() 말고 indexOf(target, startIdx)사용