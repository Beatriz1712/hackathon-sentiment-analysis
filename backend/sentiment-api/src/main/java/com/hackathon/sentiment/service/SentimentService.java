package com.hackathon.sentiment.service;

import com.hackathon.sentiment.dto.FastApiRequest;
import com.hackathon.sentiment.dto.FastApiResponse;
import com.hackathon.sentiment.dto.SentimentResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

/**
 * Service: Sentiment analysis business logic
 * Integrates with FastAPI ML service for predictions
 */
@Service
public class SentimentService {

    private final WebClient webClient;
    private final String predictEndpoint;

    public SentimentService(WebClient mlServiceWebClient,
                           @Value("${ml.service.predict-endpoint}") String predictEndpoint) {
        this.webClient = mlServiceWebClient;
        this.predictEndpoint = predictEndpoint;
    }

    public SentimentResponse analyze(String text) {
        // Create request for FastAPI
        FastApiRequest request = new FastApiRequest(text);

        // Call FastAPI ML service
        FastApiResponse response = webClient.post()
                .uri(predictEndpoint)
                .bodyValue(request)
                .retrieve()
                .bodyToMono(FastApiResponse.class)
                .block();

        // Handle null response
        if (response == null) {
            throw new RuntimeException("No response received from ML service");
        }

        // Map FastAPI response to SentimentResponse
        return new SentimentResponse(
                response.prevision(),
                response.probabilidad()
        );
    }
}
