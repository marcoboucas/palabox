"""Datatypes."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class QuestionCount:
    difficulty: str
    count: int


@dataclass
class Contributions:
    points: int
    questionCount: int
    testcaseCount: int


@dataclass
class Profile:
    realName: str
    websites: List[str]
    countryName: str
    skillTags: List[str]
    company: Optional[str]
    school: Optional[str]
    starRating: float
    aboutMe: str
    userAvatar: str
    reputation: int
    ranking: int


@dataclass
class SubmissionCount:
    difficulty: str
    count: int
    submissions: int


@dataclass
class SubmitStats:
    acSubmissionNum: List[SubmissionCount]
    totalSubmissionNum: List[SubmissionCount]


@dataclass
class MatchedUser:
    username: str
    githubUrl: str
    contributions: Contributions
    profile: Profile
    submitStats: SubmitStats


@dataclass
class LeetCodeData:
    """Data from LeetCode about one user."""

    allQuestionsCount: List[QuestionCount]
    matchedUser: MatchedUser
