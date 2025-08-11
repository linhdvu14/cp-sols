#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
const ll ALPHABET_SIZE=26;
const char MINIMAL_CHAR='a';
struct AhoCorasick
{
	const int NON_EXISTENT_NODE_ID=-1;	// if no child exists
	const int FAKE_NODE_ID=0;	// just a dummy node
	const int ROOT_ID=1;	// root of the trie (automaton)
	int currentNode;
	
	vector<array<int,ALPHABET_SIZE>> edges;	// the edges from a node to it's children
	
	vector<int> suffixLink;	// for the ith node, this points to a node j in the trie
							// which has the longest suffix of ith node == prefix of the jth node.
							// This is the failure function. If a node, does not have the required
							// child edge, then the failure function is called.
							// Just like prefix function in KMP.
							
	
	vector<ll> sum;	// for a node,it holds the sum of beauty of all occurrences
					// ending at this node.
	
	explicit AhoCorasick(const vector<pair<string,int>> &a) :currentNode(ROOT_ID),
															 edges(2),
															 suffixLink(2,FAKE_NODE_ID),sum(2,0)
	{
		// this constructor gets the set of patterns and
		// their corresponding beauties.
		// this constructor builds the automaton.
		
		edges[FAKE_NODE_ID].fill(ROOT_ID);
		edges[ROOT_ID].fill(NON_EXISTENT_NODE_ID);
		// initially assume there are no edges to the root node of the trie.
		
		for(const auto &p:a)
		// so ,every string is added to the automaton.
		{
			int node=ROOT_ID;
			// for every string, start from the root of the trie.
			for(unsigned char c : p.first)
			{
				c-=MINIMAL_CHAR;	// this is just to convert [97..122] -> [0..25]
				if(edges[node][c]==-1)
				// if there is not edge for character c.
				{
					edges[node][c]=edges.size();	// add a new node
					edges.emplace_back();
					edges.back().fill(NON_EXISTENT_NODE_ID);
					suffixLink.push_back(NON_EXISTENT_NODE_ID);
					sum.push_back(0);
				}
				node=edges[node][c];
			}
			sum[node]+=p.second;	// add beauty of this string to the end node.
		}
		
		// Perform BFS from root
		
		// to find the suffixLinks of each node
		// and to update the beauty of some nodes.
		
		// Note : If there are 2 strings {he,she}.
		//		  Then, the substring "he" occurs in 2 strings
		// 		  and the beauty of "he" should be added whereever "she" also occurs.
		//		  and the end node corresponding to "she" and "he" will be different
		//		  in the automaton.
		
		queue<int> q;
		q.push(ROOT_ID);
		while(!q.empty())
		{
			int node=q.front();
			if(suffixLink[node]!=NON_EXISTENT_NODE_ID)
			{
				// this takes care of the above Note.
				sum[node]+=sum[suffixLink[node]];
			}
			q.pop();
			for(int i=0;i<ALPHABET_SIZE;i++)
			{
				int child=edges[node][i];
				if(child==NON_EXISTENT_NODE_ID)
				{
					// assigns edge to the suffix link node.s
					edges[node][i]=edges[suffixLink[node]][i];
				}
				else
				{
					suffixLink[child]=edges[suffixLink[node]][i];
					q.push(child);
				}
			}
		}													  	
	}
	void setNode(int node)
	{
		currentNode=node;
	}
	
	void resetNode()
	{
		setNode(ROOT_ID);
	}
	
	ll getCurrentNodeSum()
	{
		return sum[currentNode];
	}
	
	void move(unsigned char c)
	{
		c-=MINIMAL_CHAR;
		currentNode=edges[currentNode][c];
	}
};
void solve()
{
	string A,B;
	cin>>A>>B;
	int N;
	cin>>N;
	vector<pair<string,int>> s(N);
	for(int i=0;i<N;i++)
	{
		cin>>s[i].first>>s[i].second;
	}
	
	AhoCorasick ahoCorasick(s);
	
	vector<ll> prefASum(A.size());	// prefix sum of beauties of A[0..i]
	vector<int> prefANode(A.size());	// prefANode[i] : denotes the
										// node at which the string A[0..i] ends
										// in the automaton. This is stored because
										// the B[j..j+24] substring can be traversed
										// from this node.  
	for(int i=0;i<A.size();i++)
	{
		ahoCorasick.move(A[i]);
		prefASum[i]=ahoCorasick.getCurrentNodeSum();
		if(i!=0)
		{
			prefASum[i]+=prefASum[i-1];
		}
		
		prefANode[i]=ahoCorasick.currentNode;
	}
	ahoCorasick.resetNode();
	vector<ll> suffBSum(B.size());
	for(int i=0;i<B.size();i++)
	{
		ahoCorasick.move(B[i]);
		suffBSum[i]=ahoCorasick.getCurrentNodeSum();
	}
	for(int i=(int)B.size()-2;i>=0;i--)
	{
		suffBSum[i]+=suffBSum[i+1];
	}
	ll ans=0;
	for(int i=0;i<A.size();i++)
	{
		for(int j=0;j<B.size();j++)
		{
			ll cur=prefASum[i];
			ahoCorasick.setNode(prefANode[i]);
			for(int k=j;k<j+25&&k<(int)B.size();k++)
			{
				ahoCorasick.move(B[k]);
				cur+=ahoCorasick.getCurrentNodeSum();
			}
			if(j+25<(int)B.size())
			{
				cur+=suffBSum[j+25];
			}
			ans=max(ans,cur);
		}
	}
	cout<<ans<<"\n";
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll T=1,p=0;
	cin>>T;
	do
	{
		solve();
		p++;
	}while(p<T);
	return 0;
}

