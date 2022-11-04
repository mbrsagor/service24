class WorkTrackerAddListAPIView(generics.ListCreateAPIView):
    """
    Name: Time treacker add and listview
    Desc: All assign issue list of time tracker listview.
    """
    queryset = WorkTracker.objects.all()
    serializer_class = serializers.WorkTrackerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('assign_issue',)
    search_fields = ('assign_issue',)

    def get(self, request, *args, **kwargs):
        trackedData = []
        obj = WorkTracker.objects.all()
        filter_backends = self.filter_queryset(obj)
        serializer = serializers.WorkTrackerSerializer(filter_backends, many=True)

